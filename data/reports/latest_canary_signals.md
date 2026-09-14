# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T13:52:40.971629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.111` n `12`; crypto_alt avg `0.2068` n `233`; crypto_major avg `0.147` n `8`; equity avg `0.3683` n `136`; fx avg `-0.0077` n `6`; index avg `0.0642` n `27`; metal avg `0.01` n `20`; unknown avg `-0.0065` n `880`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.1689` n `233`; crypto_major avg `0.2783` n `8`; equity avg `0.4988` n `136`; fx avg `0.0063` n `6`; index avg `0.0668` n `27`; metal avg `-0.0043` n `20`; unknown avg `1.5067` n `878`
- 4h: commodity avg `0.1081` n `12`; crypto_alt avg `-0.6207` n `233`; crypto_major avg `-0.3037` n `8`; equity avg `0.126` n `136`; fx avg `0.0719` n `6`; index avg `0.0568` n `27`; metal avg `0.0582` n `20`; unknown avg `0.5879` n `872`
- 24h: commodity avg `0.5933` n `12`; crypto_alt avg `-0.5482` n `233`; crypto_major avg `1.5792` n `8`; equity avg `-0.829` n `136`; fx avg `0.0892` n `6`; index avg `-0.221` n `27`; metal avg `-0.475` n `20`; unknown avg `1.4355` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
