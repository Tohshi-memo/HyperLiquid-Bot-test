# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T10:52:27.227088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0726` n `12`; crypto_alt avg `0.2817` n `231`; crypto_major avg `0.2929` n `8`; equity avg `0.0339` n `122`; fx avg `-0.0071` n `6`; index avg `-0.0032` n `25`; metal avg `0.0166` n `20`; unknown avg `0.0572` n `795`
- 1h: commodity avg `0.1294` n `12`; crypto_alt avg `0.1468` n `231`; crypto_major avg `0.1907` n `8`; equity avg `-0.0197` n `122`; fx avg `-0.0227` n `6`; index avg `-0.0294` n `25`; metal avg `-0.0569` n `20`; unknown avg `0.0897` n `794`
- 4h: commodity avg `-0.3038` n `12`; crypto_alt avg `-0.7009` n `231`; crypto_major avg `-0.8094` n `8`; equity avg `0.5408` n `122`; fx avg `-0.0121` n `6`; index avg `0.085` n `25`; metal avg `-0.1023` n `20`; unknown avg `-0.1465` n `794`
- 24h: commodity avg `-0.6209` n `12`; crypto_alt avg `0.5594` n `231`; crypto_major avg `1.4918` n `8`; equity avg `0.8044` n `122`; fx avg `0.0046` n `6`; index avg `0.146` n `25`; metal avg `-0.21` n `20`; unknown avg `-0.0695` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
