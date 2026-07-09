# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T13:52:30.038689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0877` n `12`; crypto_alt avg `0.2727` n `229`; crypto_major avg `0.3595` n `8`; equity avg `0.3503` n `91`; fx avg `0.0028` n `6`; index avg `0.0277` n `25`; metal avg `0.1116` n `20`; unknown avg `0.0669` n `765`
- 1h: commodity avg `-0.4748` n `12`; crypto_alt avg `0.2384` n `229`; crypto_major avg `0.5122` n `8`; equity avg `0.6662` n `91`; fx avg `-0.0095` n `6`; index avg `0.1395` n `25`; metal avg `0.2249` n `20`; unknown avg `0.1355` n `765`
- 4h: commodity avg `-0.2939` n `12`; crypto_alt avg `0.2411` n `229`; crypto_major avg `0.155` n `8`; equity avg `1.0921` n `91`; fx avg `-0.0363` n `6`; index avg `0.3002` n `25`; metal avg `0.321` n `20`; unknown avg `0.1527` n `764`
- 24h: commodity avg `-0.5567` n `12`; crypto_alt avg `1.6055` n `229`; crypto_major avg `1.0841` n `8`; equity avg `2.6833` n `91`; fx avg `0.0887` n `6`; index avg `0.4846` n `25`; metal avg `0.8607` n `20`; unknown avg `0.8547` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0968`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0657`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0637`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0616`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0612`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0604`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0602`, n `669`, weak_sample_signal
