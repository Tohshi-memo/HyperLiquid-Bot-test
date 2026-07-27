# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T00:22:31.166030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1224` n `12`; crypto_alt avg `0.0031` n `230`; crypto_major avg `-0.1045` n `8`; equity avg `0.0172` n `100`; fx avg `0.0229` n `6`; index avg `0.0158` n `25`; metal avg `0.0184` n `20`; unknown avg `0.0311` n `775`
- 1h: commodity avg `-0.1518` n `12`; crypto_alt avg `-0.0055` n `230`; crypto_major avg `-0.2311` n `8`; equity avg `-0.2565` n `100`; fx avg `0.0346` n `6`; index avg `-0.0696` n `25`; metal avg `0.1187` n `20`; unknown avg `0.0161` n `775`
- 4h: commodity avg `-0.4633` n `12`; crypto_alt avg `0.8496` n `230`; crypto_major avg `0.8375` n `8`; equity avg `0.324` n `100`; fx avg `0.0271` n `6`; index avg `0.0675` n `25`; metal avg `0.2759` n `20`; unknown avg `0.0234` n `775`
- 24h: commodity avg `-0.6459` n `12`; crypto_alt avg `1.6505` n `230`; crypto_major avg `1.5748` n `8`; equity avg `0.7985` n `100`; fx avg `0.0846` n `6`; index avg `0.1388` n `25`; metal avg `0.4647` n `20`; unknown avg `0.068` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
