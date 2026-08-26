# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T04:37:33.004516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.1154` n `231`; crypto_major avg `0.0625` n `8`; equity avg `-0.0189` n `122`; fx avg `0.0154` n `6`; index avg `0.0011` n `25`; metal avg `-0.0085` n `20`; unknown avg `0.0871` n `797`
- 1h: commodity avg `0.0359` n `12`; crypto_alt avg `0.2033` n `231`; crypto_major avg `0.1294` n `8`; equity avg `0.1799` n `122`; fx avg `-0.014` n `6`; index avg `0.0296` n `25`; metal avg `-0.0602` n `20`; unknown avg `0.2982` n `797`
- 4h: commodity avg `-0.0983` n `12`; crypto_alt avg `1.2148` n `231`; crypto_major avg `0.9823` n `8`; equity avg `0.6203` n `122`; fx avg `-0.0362` n `6`; index avg `0.1627` n `25`; metal avg `0.1225` n `20`; unknown avg `1.2024` n `796`
- 24h: commodity avg `-0.8054` n `12`; crypto_alt avg `-2.3895` n `231`; crypto_major avg `-2.3091` n `8`; equity avg `1.4127` n `122`; fx avg `0.0102` n `6`; index avg `0.2054` n `25`; metal avg `0.3025` n `20`; unknown avg `0.4051` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
