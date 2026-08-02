# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T00:52:31.086428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0752` n `12`; crypto_alt avg `0.0762` n `230`; crypto_major avg `0.0182` n `8`; equity avg `-0.0111` n `102`; fx avg `0.0092` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.6476` n `782`
- 1h: commodity avg `0.0843` n `12`; crypto_alt avg `0.255` n `230`; crypto_major avg `0.0765` n `8`; equity avg `0.2853` n `102`; fx avg `0.0763` n `6`; index avg `0.0427` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.1951` n `782`
- 4h: commodity avg `-0.202` n `12`; crypto_alt avg `0.5044` n `230`; crypto_major avg `0.4374` n `8`; equity avg `0.5875` n `102`; fx avg `0.0008` n `6`; index avg `0.0866` n `25`; metal avg `0.0586` n `20`; unknown avg `0.3537` n `782`
- 24h: commodity avg `-0.1754` n `12`; crypto_alt avg `-0.7778` n `230`; crypto_major avg `-0.8532` n `8`; equity avg `0.1323` n `102`; fx avg `-0.0415` n `6`; index avg `0.063` n `25`; metal avg `0.0623` n `20`; unknown avg `-0.0558` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
