# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T17:52:33.592229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0479` n `12`; crypto_alt avg `-0.0536` n `230`; crypto_major avg `-0.0404` n `8`; equity avg `-0.1472` n `100`; fx avg `-0.0017` n `6`; index avg `-0.0294` n `25`; metal avg `-0.0481` n `20`; unknown avg `-0.0568` n `773`
- 1h: commodity avg `0.034` n `12`; crypto_alt avg `0.4299` n `230`; crypto_major avg `0.3812` n `8`; equity avg `0.0252` n `100`; fx avg `-0.0181` n `6`; index avg `0.0068` n `25`; metal avg `0.0012` n `20`; unknown avg `0.1297` n `773`
- 4h: commodity avg `-0.3034` n `12`; crypto_alt avg `0.4339` n `230`; crypto_major avg `0.3591` n `8`; equity avg `0.0152` n `100`; fx avg `-0.0165` n `6`; index avg `0.0738` n `25`; metal avg `0.0953` n `20`; unknown avg `13.3565` n `773`
- 24h: commodity avg `-0.7949` n `12`; crypto_alt avg `-1.0087` n `230`; crypto_major avg `-0.8436` n `8`; equity avg `-2.5326` n `100`; fx avg `-0.1591` n `6`; index avg `-0.2652` n `25`; metal avg `0.1252` n `20`; unknown avg `14.0677` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1216`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1185`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1106`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1041`, n `666`, weak_sample_signal
