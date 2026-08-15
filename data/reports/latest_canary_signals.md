# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T01:37:24.292722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `0.0283` n `230`; crypto_major avg `0.0563` n `8`; equity avg `0.0079` n `114`; fx avg `0.0006` n `6`; index avg `0.0054` n `25`; metal avg `-0.0041` n `20`; unknown avg `0.1705` n `791`
- 1h: commodity avg `-0.0968` n `12`; crypto_alt avg `-0.0955` n `230`; crypto_major avg `0.0777` n `8`; equity avg `0.0293` n `114`; fx avg `-0.0076` n `6`; index avg `0.0057` n `25`; metal avg `-0.0286` n `20`; unknown avg `0.186` n `791`
- 4h: commodity avg `-0.0033` n `12`; crypto_alt avg `0.2787` n `230`; crypto_major avg `0.3915` n `8`; equity avg `0.0169` n `114`; fx avg `-0.0183` n `6`; index avg `-0.0105` n `25`; metal avg `0.0522` n `20`; unknown avg `2.9526` n `791`
- 24h: commodity avg `0.1785` n `12`; crypto_alt avg `0.0202` n `230`; crypto_major avg `-0.6226` n `8`; equity avg `-0.1387` n `114`; fx avg `0.0908` n `6`; index avg `-0.009` n `25`; metal avg `0.4748` n `20`; unknown avg `-0.3243` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
