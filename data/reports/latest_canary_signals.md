# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T10:52:31.371826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `0.0093` n `234`; crypto_major avg `-0.0808` n `8`; equity avg `-0.0162` n `137`; fx avg `-0.0122` n `6`; index avg `-0.0055` n `27`; metal avg `0.0491` n `20`; unknown avg `0.2101` n `921`
- 1h: commodity avg `-0.1081` n `12`; crypto_alt avg `-0.1619` n `234`; crypto_major avg `-0.328` n `8`; equity avg `0.088` n `137`; fx avg `-0.0034` n `6`; index avg `0.0226` n `27`; metal avg `0.0876` n `20`; unknown avg `0.3011` n `919`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `0.0858` n `234`; crypto_major avg `-0.1852` n `8`; equity avg `0.6596` n `137`; fx avg `0.0453` n `6`; index avg `0.0874` n `27`; metal avg `0.079` n `20`; unknown avg `0.162` n `911`
- 24h: commodity avg `-0.6403` n `12`; crypto_alt avg `2.9416` n `234`; crypto_major avg `1.2219` n `8`; equity avg `1.5483` n `137`; fx avg `0.0899` n `6`; index avg `0.1252` n `27`; metal avg `-0.1188` n `20`; unknown avg `0.4644` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
