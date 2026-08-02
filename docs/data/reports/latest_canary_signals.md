# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T14:52:24.239895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `-0.0349` n `230`; crypto_major avg `-0.003` n `8`; equity avg `-0.0181` n `102`; fx avg `0.0036` n `6`; index avg `0.0038` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.0333` n `782`
- 1h: commodity avg `-0.0638` n `12`; crypto_alt avg `0.1209` n `230`; crypto_major avg `0.1079` n `8`; equity avg `0.0219` n `102`; fx avg `-0.0129` n `6`; index avg `0.0039` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0025` n `782`
- 4h: commodity avg `-0.0645` n `12`; crypto_alt avg `-0.0153` n `230`; crypto_major avg `-0.0317` n `8`; equity avg `-0.2433` n `102`; fx avg `-0.0269` n `6`; index avg `-0.0221` n `25`; metal avg `0.0097` n `20`; unknown avg `-0.1137` n `782`
- 24h: commodity avg `-1.0659` n `12`; crypto_alt avg `0.2249` n `230`; crypto_major avg `0.1161` n `8`; equity avg `0.8305` n `102`; fx avg `-0.1444` n `6`; index avg `0.2152` n `25`; metal avg `0.2626` n `20`; unknown avg `0.2314` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
