# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T22:22:24.898898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `5.6732` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `5.1488` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `4.266` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.06` n `230`; crypto_major avg `-0.1095` n `8`; equity avg `0.0533` n `121`; fx avg `-0.0011` n `6`; index avg `0.015` n `25`; metal avg `0.0057` n `20`; unknown avg `0.0135` n `792`
- 1h: commodity avg `-0.0537` n `12`; crypto_alt avg `-0.3763` n `230`; crypto_major avg `0.0208` n `8`; equity avg `0.1543` n `121`; fx avg `0.0008` n `6`; index avg `0.046` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.1222` n `792`
- 4h: commodity avg `-0.1872` n `12`; crypto_alt avg `2.4954` n `230`; crypto_major avg `5.486` n `8`; equity avg `1.22` n `121`; fx avg `-0.0196` n `6`; index avg `0.1303` n `25`; metal avg `0.3372` n `20`; unknown avg `1.1492` n `792`
- 24h: commodity avg `-0.1078` n `12`; crypto_alt avg `5.5135` n `230`; crypto_major avg `10.6007` n `8`; equity avg `0.7411` n `120`; fx avg `-0.2251` n `6`; index avg `0.1029` n `25`; metal avg `1.2927` n `20`; unknown avg `1.4671` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
