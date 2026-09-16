# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T00:37:25.243515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.0255` n `234`; crypto_major avg `0.0874` n `8`; equity avg `0.0437` n `137`; fx avg `0.0458` n `6`; index avg `0.0172` n `27`; metal avg `-0.0283` n `20`; unknown avg `0.2801` n `913`
- 1h: commodity avg `-0.1047` n `12`; crypto_alt avg `0.075` n `234`; crypto_major avg `0.2237` n `8`; equity avg `0.1412` n `137`; fx avg `0.0802` n `6`; index avg `0.0376` n `27`; metal avg `-0.0416` n `20`; unknown avg `-0.0148` n `911`
- 4h: commodity avg `-0.0703` n `12`; crypto_alt avg `-0.0983` n `234`; crypto_major avg `0.1555` n `8`; equity avg `0.0599` n `137`; fx avg `0.0852` n `6`; index avg `0.0329` n `27`; metal avg `-0.0225` n `20`; unknown avg `0.2819` n `861`
- 24h: commodity avg `0.2755` n `12`; crypto_alt avg `-3.8174` n `234`; crypto_major avg `-3.8495` n `8`; equity avg `-1.4187` n `137`; fx avg `0.2794` n `6`; index avg `-0.1183` n `27`; metal avg `0.2461` n `20`; unknown avg `0.6588` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
