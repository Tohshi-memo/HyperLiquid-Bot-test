# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T02:52:36.857259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0469` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `0.1225` n `230`; crypto_major avg `0.1645` n `8`; equity avg `0.1263` n `102`; fx avg `-0.0066` n `6`; index avg `0.0311` n `25`; metal avg `0.0357` n `20`; unknown avg `-0.095` n `782`
- 1h: commodity avg `-0.6198` n `12`; crypto_alt avg `0.4928` n `230`; crypto_major avg `0.6582` n `8`; equity avg `0.8324` n `102`; fx avg `0.0024` n `6`; index avg `0.1599` n `25`; metal avg `0.0973` n `20`; unknown avg `1.0209` n `782`
- 4h: commodity avg `-0.8853` n `12`; crypto_alt avg `1.0965` n `230`; crypto_major avg `1.1616` n `8`; equity avg `1.0539` n `102`; fx avg `-0.0078` n `6`; index avg `0.2302` n `25`; metal avg `0.1264` n `20`; unknown avg `1.5759` n `782`
- 24h: commodity avg `-0.8928` n `12`; crypto_alt avg `0.0364` n `230`; crypto_major avg `0.1607` n `8`; equity avg `0.8439` n `102`; fx avg `-0.0405` n `6`; index avg `0.1749` n `25`; metal avg `0.1944` n `20`; unknown avg `-0.0466` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
