# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T20:00:27.625989+00:00`
- Correlation status: `ready`
- Asset price records: `103`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `7`; crypto_alt avg `0.0114` n `223`; crypto_major avg `-0.0407` n `7`; equity avg `0.0205` n `42`; fx avg `0.0032` n `4`; index avg `-0.0067` n `9`; metal avg `0.0001` n `7`; unknown avg `-0.1452` n `313`
- 1h: commodity avg `-0.0515` n `7`; crypto_alt avg `0.2218` n `223`; crypto_major avg `-0.0447` n `7`; equity avg `0.1346` n `42`; fx avg `0.0074` n `4`; index avg `0.0121` n `9`; metal avg `-0.0056` n `7`; unknown avg `-0.0593` n `313`
- 4h: commodity avg `-0.1824` n `7`; crypto_alt avg `0.4776` n `223`; crypto_major avg `0.0064` n `7`; equity avg `0.2609` n `42`; fx avg `0.0415` n `4`; index avg `0.0412` n `9`; metal avg `-0.0298` n `7`; unknown avg `-0.0476` n `313`
- 24h: commodity avg `-0.0279` n `7`; crypto_alt avg `1.6405` n `223`; crypto_major avg `0.2535` n `7`; equity avg `0.8745` n `42`; fx avg `-0.0202` n `4`; index avg `0.0617` n `9`; metal avg `-0.0932` n `7`; unknown avg `0.1686` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5237`, n `95`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5086`, n `95`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5085`, n `99`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4909`, n `99`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.444`, n `95`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4277`, n `95`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4242`, n `95`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4217`, n `99`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4176`, n `95`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4169`, n `95`, moderate_sample_signal
