# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T00:37:28.454131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0707` n `12`; crypto_alt avg `-0.0869` n `230`; crypto_major avg `-0.1151` n `8`; equity avg `-0.0319` n `100`; fx avg `0.0164` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.0329` n `775`
- 1h: commodity avg `-0.0454` n `12`; crypto_alt avg `-0.1931` n `230`; crypto_major avg `-0.3868` n `8`; equity avg `-0.2997` n `100`; fx avg `0.0498` n `6`; index avg `-0.0864` n `25`; metal avg `0.1014` n `20`; unknown avg `0.0189` n `775`
- 4h: commodity avg `-0.4032` n `12`; crypto_alt avg `0.7734` n `230`; crypto_major avg `0.7291` n `8`; equity avg `0.3007` n `100`; fx avg `0.0406` n `6`; index avg `0.0641` n `25`; metal avg `0.2728` n `20`; unknown avg `0.0045` n `775`
- 24h: commodity avg `-0.5573` n `12`; crypto_alt avg `1.5617` n `230`; crypto_major avg `1.5077` n `8`; equity avg `0.8023` n `100`; fx avg `0.0887` n `6`; index avg `0.132` n `25`; metal avg `0.4468` n `20`; unknown avg `0.0573` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
