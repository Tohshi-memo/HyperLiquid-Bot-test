# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T06:22:26.217197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.06` n `12`; crypto_alt avg `0.2361` n `228`; crypto_major avg `0.2337` n `8`; equity avg `0.0737` n `88`; fx avg `0.0541` n `6`; index avg `0.0262` n `23`; metal avg `0.0179` n `20`; unknown avg `0.0855` n `764`
- 1h: commodity avg `0.0638` n `12`; crypto_alt avg `0.9453` n `228`; crypto_major avg `1.1716` n `8`; equity avg `0.5239` n `88`; fx avg `0.0012` n `6`; index avg `0.1288` n `23`; metal avg `0.2073` n `20`; unknown avg `0.3475` n `732`
- 4h: commodity avg `-0.0549` n `12`; crypto_alt avg `1.3566` n `228`; crypto_major avg `1.3573` n `8`; equity avg `0.676` n `88`; fx avg `0.0254` n `6`; index avg `0.1797` n `23`; metal avg `0.0417` n `20`; unknown avg `0.0868` n `732`
- 24h: commodity avg `-0.3003` n `12`; crypto_alt avg `1.0495` n `228`; crypto_major avg `1.0422` n `8`; equity avg `0.4712` n `88`; fx avg `0.0534` n `6`; index avg `0.1219` n `23`; metal avg `-0.1132` n `20`; unknown avg `-0.7334` n `718`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
