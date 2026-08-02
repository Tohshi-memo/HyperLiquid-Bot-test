# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T04:37:30.080770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3502` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0132` n `12`; crypto_alt avg `0.0306` n `230`; crypto_major avg `-0.0108` n `8`; equity avg `-0.0409` n `102`; fx avg `0.0164` n `6`; index avg `-0.0171` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.1479` n `782`
- 1h: commodity avg `0.0466` n `12`; crypto_alt avg `0.0784` n `230`; crypto_major avg `0.0906` n `8`; equity avg `0.016` n `102`; fx avg `-0.0138` n `6`; index avg `-0.0012` n `25`; metal avg `0.0403` n `20`; unknown avg `0.0325` n `782`
- 4h: commodity avg `-1.0118` n `12`; crypto_alt avg `1.0424` n `230`; crypto_major avg `1.3384` n `8`; equity avg `0.6804` n `102`; fx avg `-0.0354` n `6`; index avg `0.1874` n `25`; metal avg `0.2028` n `20`; unknown avg `4.7667` n `782`
- 24h: commodity avg `-1.1791` n `12`; crypto_alt avg `0.0235` n `230`; crypto_major avg `0.3778` n `8`; equity avg `0.8181` n `102`; fx avg `-0.1002` n `6`; index avg `0.2055` n `25`; metal avg `0.2816` n `20`; unknown avg `0.0104` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
