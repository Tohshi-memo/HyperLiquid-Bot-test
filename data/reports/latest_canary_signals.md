# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T05:22:31.575899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0534` n `12`; crypto_alt avg `0.1284` n `230`; crypto_major avg `0.1108` n `8`; equity avg `0.1269` n `100`; fx avg `0.0077` n `6`; index avg `0.0382` n `25`; metal avg `-0.0105` n `20`; unknown avg `0.1827` n `775`
- 1h: commodity avg `-0.0484` n `12`; crypto_alt avg `-0.0447` n `230`; crypto_major avg `-0.0246` n `8`; equity avg `0.2068` n `100`; fx avg `0.0024` n `6`; index avg `0.0633` n `25`; metal avg `0.035` n `20`; unknown avg `7.547` n `775`
- 4h: commodity avg `-0.1548` n `12`; crypto_alt avg `0.2596` n `230`; crypto_major avg `0.4491` n `8`; equity avg `0.7231` n `100`; fx avg `0.0312` n `6`; index avg `0.1714` n `25`; metal avg `-0.0675` n `20`; unknown avg `-0.2997` n `775`
- 24h: commodity avg `-0.5397` n `12`; crypto_alt avg `1.1614` n `230`; crypto_major avg `1.3319` n `8`; equity avg `1.0797` n `100`; fx avg `0.0803` n `6`; index avg `0.1545` n `25`; metal avg `0.3389` n `20`; unknown avg `-0.0121` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
