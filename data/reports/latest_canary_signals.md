# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T15:52:31.485705+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.0792` n `231`; crypto_major avg `-0.0531` n `8`; equity avg `-0.0627` n `122`; fx avg `0.0058` n `6`; index avg `-0.0219` n `25`; metal avg `-0.0185` n `20`; unknown avg `0.0179` n `795`
- 1h: commodity avg `-0.0421` n `12`; crypto_alt avg `-0.2444` n `231`; crypto_major avg `-0.0454` n `8`; equity avg `0.0745` n `122`; fx avg `-0.007` n `6`; index avg `0.0204` n `25`; metal avg `0.0981` n `20`; unknown avg `0.0381` n `795`
- 4h: commodity avg `-0.0837` n `12`; crypto_alt avg `-0.5565` n `231`; crypto_major avg `-0.1305` n `8`; equity avg `0.2501` n `122`; fx avg `0.0253` n `6`; index avg `-0.0725` n `25`; metal avg `0.1171` n `20`; unknown avg `-0.0184` n `795`
- 24h: commodity avg `-0.6754` n `12`; crypto_alt avg `-1.2997` n `231`; crypto_major avg `-0.1328` n `8`; equity avg `1.4709` n `122`; fx avg `0.0273` n `6`; index avg `0.1697` n `25`; metal avg `-0.148` n `20`; unknown avg `-0.9506` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
