# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T11:11:33.124302+00:00`
- Correlation status: `ready`
- Asset price records: `67`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0375` n `7`; crypto_alt avg `-0.1784` n `223`; crypto_major avg `-0.0589` n `7`; equity avg `-0.0108` n `42`; fx avg `-0.0035` n `4`; index avg `0.0064` n `9`; metal avg `0.0082` n `7`; unknown avg `0.0691` n `313`
- 1h: commodity avg `0.0283` n `7`; crypto_alt avg `-0.1801` n `223`; crypto_major avg `-0.1612` n `7`; equity avg `0.0393` n `42`; fx avg `0.0027` n `4`; index avg `0.0102` n `9`; metal avg `0.0045` n `7`; unknown avg `-0.0253` n `313`
- 4h: commodity avg `0.0536` n `7`; crypto_alt avg `0.1793` n `223`; crypto_major avg `-0.0702` n `7`; equity avg `-0.0519` n `42`; fx avg `0.051` n `4`; index avg `-0.0328` n `9`; metal avg `0.0588` n `7`; unknown avg `0.1853` n `311`
- 24h: crypto_alt avg `0.7073` n `223`; crypto_major avg `0.5927` n `7`; metal avg `0.7862` n `1`; unknown avg `1.4134` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5753`, n `63`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5565`, n `59`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5554`, n `63`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5455`, n `59`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4819`, n `63`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4743`, n `59`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4713`, n `59`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4609`, n `59`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4455`, n `63`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4382`, n `63`, moderate_sample_signal
