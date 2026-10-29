# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T13:37:29.303947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6079` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1062` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.01` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0277` n `13`; crypto_alt avg `-0.2318` n `238`; crypto_major avg `-0.23` n `8`; equity avg `-0.1893` n `156`; fx avg `-0.0028` n `6`; index avg `-0.1108` n `27`; metal avg `-0.0602` n `20`; unknown avg `8.0377` n `1236`
- 1h: commodity avg `-0.348` n `13`; crypto_alt avg `0.1891` n `238`; crypto_major avg `0.4348` n `8`; equity avg `0.1353` n `156`; fx avg `-0.0667` n `6`; index avg `-0.0776` n `27`; metal avg `-0.0551` n `20`; unknown avg `5.0797` n `1230`
- 4h: commodity avg `-0.5991` n `13`; crypto_alt avg `1.2859` n `238`; crypto_major avg `2.0088` n `8`; equity avg `-0.0012` n `155`; fx avg `-0.0064` n `6`; index avg `-0.1429` n `27`; metal avg `-0.0974` n `20`; unknown avg `20.3041` n `1138`
- 24h: commodity avg `-0.8547` n `13`; crypto_alt avg `-0.7123` n `238`; crypto_major avg `0.7777` n `8`; equity avg `-0.9878` n `155`; fx avg `-0.0478` n `6`; index avg `-0.2005` n `27`; metal avg `-0.5909` n `20`; unknown avg `9.7285` n `980`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
