# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T03:22:30.314616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5227` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0706` n `12`; crypto_alt avg `0.0276` n `230`; crypto_major avg `0.0456` n `8`; equity avg `-0.0864` n `102`; fx avg `0.005` n `6`; index avg `-0.0096` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.1364` n `782`
- 1h: commodity avg `-0.2904` n `12`; crypto_alt avg `0.0228` n `230`; crypto_major avg `0.1806` n `8`; equity avg `-0.1629` n `102`; fx avg `-0.0058` n `6`; index avg `0.0145` n `25`; metal avg `0.0694` n `20`; unknown avg `-0.3364` n `782`
- 4h: commodity avg `-1.2045` n `12`; crypto_alt avg `1.1773` n `230`; crypto_major avg `1.3182` n `8`; equity avg `0.9555` n `102`; fx avg `0.0061` n `6`; index avg `0.2122` n `25`; metal avg `0.1412` n `20`; unknown avg `2.4724` n `782`
- 24h: commodity avg `-1.2218` n `12`; crypto_alt avg `0.1354` n `230`; crypto_major avg `0.3471` n `8`; equity avg `0.7666` n `102`; fx avg `-0.0763` n `6`; index avg `0.1832` n `25`; metal avg `0.2047` n `20`; unknown avg `-0.0671` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
