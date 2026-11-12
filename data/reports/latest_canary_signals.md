# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T11:22:23.416078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `-0.0543` n `239`; crypto_major avg `-0.115` n `8`; equity avg `-0.0129` n `162`; fx avg `-0.0101` n `6`; index avg `-0.0019` n `27`; metal avg `-0.0271` n `20`; unknown avg `0.3356` n `1261`
- 1h: commodity avg `-0.0381` n `13`; crypto_alt avg `-0.1878` n `239`; crypto_major avg `-0.3262` n `8`; equity avg `-0.2585` n `162`; fx avg `-0.0091` n `6`; index avg `-0.0256` n `27`; metal avg `-0.0422` n `20`; unknown avg `0.8916` n `1249`
- 4h: commodity avg `-0.1872` n `13`; crypto_alt avg `-0.0958` n `239`; crypto_major avg `-0.0609` n `8`; equity avg `0.2948` n `162`; fx avg `0.0024` n `6`; index avg `0.0456` n `27`; metal avg `-0.1403` n `20`; unknown avg `0.0314` n `1233`
- 24h: commodity avg `-0.0573` n `13`; crypto_alt avg `-1.8042` n `239`; crypto_major avg `-1.1734` n `8`; equity avg `-1.1083` n `162`; fx avg `-0.0956` n `6`; index avg `-0.0805` n `27`; metal avg `-0.9253` n `20`; unknown avg `-0.0146` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
