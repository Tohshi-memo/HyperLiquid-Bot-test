# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T03:37:31.035803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0379` n `12`; crypto_alt avg `-0.0357` n `230`; crypto_major avg `0.0447` n `8`; equity avg `-0.0573` n `100`; fx avg `0.0035` n `6`; index avg `-0.0471` n `25`; metal avg `-0.0191` n `20`; unknown avg `-0.1277` n `775`
- 1h: commodity avg `-0.0669` n `12`; crypto_alt avg `-0.077` n `230`; crypto_major avg `-0.0382` n `8`; equity avg `0.0814` n `100`; fx avg `-0.0099` n `6`; index avg `-0.0087` n `25`; metal avg `-0.0657` n `20`; unknown avg `1.055` n `775`
- 4h: commodity avg `0.0031` n `12`; crypto_alt avg `-0.1371` n `230`; crypto_major avg `-0.3546` n `8`; equity avg `-0.1677` n `100`; fx avg `0.0957` n `6`; index avg `-0.1356` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.1655` n `775`
- 24h: commodity avg `-0.5086` n `12`; crypto_alt avg `1.2039` n `230`; crypto_major avg `1.1709` n `8`; equity avg `0.7201` n `100`; fx avg `0.1324` n `6`; index avg `0.0596` n `25`; metal avg `0.3251` n `20`; unknown avg `-0.0331` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
