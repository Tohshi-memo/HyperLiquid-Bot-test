# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T17:22:27.724538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.425` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0381` n `12`; crypto_alt avg `-0.0308` n `228`; crypto_major avg `-0.132` n `8`; equity avg `-0.2056` n `66`; fx avg `-0.009` n `5`; index avg `-0.1007` n `23`; metal avg `-0.0594` n `18`; unknown avg `-0.0664` n `384`
- 1h: commodity avg `0.0399` n `12`; crypto_alt avg `0.1608` n `228`; crypto_major avg `0.1827` n `8`; equity avg `-0.3378` n `66`; fx avg `-0.0266` n `5`; index avg `-0.1448` n `23`; metal avg `0.1401` n `18`; unknown avg `0.0224` n `384`
- 4h: commodity avg `1.3248` n `12`; crypto_alt avg `-0.6342` n `228`; crypto_major avg `-1.1002` n `8`; equity avg `-2.2835` n `66`; fx avg `-0.0162` n `5`; index avg `-0.9847` n `23`; metal avg `-0.1661` n `18`; unknown avg `-0.1905` n `383`
- 24h: commodity avg `1.0822` n `12`; crypto_alt avg `-2.0122` n `228`; crypto_major avg `-1.5445` n `8`; equity avg `-0.8753` n `66`; fx avg `0.0167` n `5`; index avg `-0.4249` n `23`; metal avg `0.7046` n `18`; unknown avg `-0.2451` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
