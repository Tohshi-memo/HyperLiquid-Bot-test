# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T03:52:32.091871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1936` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0996` n `12`; crypto_alt avg `-0.0608` n `230`; crypto_major avg `-0.0632` n `8`; equity avg `-0.0061` n `102`; fx avg `-0.0098` n `6`; index avg `0.0019` n `25`; metal avg `0.0046` n `20`; unknown avg `-0.0387` n `782`
- 1h: commodity avg `-0.2136` n `12`; crypto_alt avg `-0.0947` n `230`; crypto_major avg `0.0498` n `8`; equity avg `-0.1071` n `102`; fx avg `-0.0382` n `6`; index avg `0.0267` n `25`; metal avg `0.0351` n `20`; unknown avg `-0.3234` n `782`
- 4h: commodity avg `-0.9528` n `12`; crypto_alt avg `1.0807` n `230`; crypto_major avg `1.2408` n `8`; equity avg `0.9578` n `102`; fx avg `0.0357` n `6`; index avg `0.242` n `25`; metal avg `0.1637` n `20`; unknown avg `2.2848` n `782`
- 24h: commodity avg `-1.1696` n `12`; crypto_alt avg `0.0092` n `230`; crypto_major avg `0.3124` n `8`; equity avg `0.8247` n `102`; fx avg `-0.102` n `6`; index avg `0.2445` n `25`; metal avg `0.2315` n `20`; unknown avg `-0.0483` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
