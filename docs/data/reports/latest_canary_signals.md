# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T01:22:16.385390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.4092` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.6196` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2699` n `12`; crypto_alt avg `-0.2326` n `228`; crypto_major avg `-0.3243` n `8`; equity avg `-0.1562` n `66`; fx avg `-0.0149` n `5`; index avg `-0.0601` n `23`; metal avg `0.171` n `18`; unknown avg `-0.0451` n `383`
- 1h: commodity avg `0.6316` n `12`; crypto_alt avg `-0.0377` n `228`; crypto_major avg `-0.3559` n `8`; equity avg `-0.0554` n `66`; fx avg `0.0281` n `5`; index avg `0.0553` n `23`; metal avg `-0.9522` n `18`; unknown avg `0.6693` n `383`
- 4h: commodity avg `1.2728` n `12`; crypto_alt avg `-2.476` n `228`; crypto_major avg `-2.1364` n `8`; equity avg `-0.8444` n `66`; fx avg `0.0611` n `5`; index avg `-0.5168` n `23`; metal avg `-0.8945` n `18`; unknown avg `2.2881` n `383`
- 24h: commodity avg `2.991` n `12`; crypto_alt avg `-11.1574` n `228`; crypto_major avg `-3.2755` n `8`; equity avg `-3.6378` n `65`; fx avg `-0.1203` n `5`; index avg `-1.9815` n `23`; metal avg `-6.7776` n `18`; unknown avg `550.9487` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
