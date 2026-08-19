# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T16:43:30.580327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `5.0528` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `4.5051` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.109` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `0.0872` n `230`; crypto_major avg `0.018` n `8`; equity avg `-0.0172` n `121`; fx avg `-0.017` n `6`; index avg `-0.0334` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0113` n `792`
- 1h: commodity avg `0.0018` n `12`; crypto_alt avg `-0.2827` n `230`; crypto_major avg `0.2952` n `8`; equity avg `0.3598` n `121`; fx avg `-0.0146` n `6`; index avg `-0.0129` n `25`; metal avg `0.1266` n `20`; unknown avg `0.0467` n `792`
- 4h: commodity avg `0.2031` n `12`; crypto_alt avg `2.5477` n `230`; crypto_major avg `4.7082` n `8`; equity avg `-0.3446` n `120`; fx avg `0.1051` n `6`; index avg `-0.081` n `25`; metal avg `0.5992` n `20`; unknown avg `0.9483` n `792`
- 24h: commodity avg `0.3155` n `12`; crypto_alt avg `2.7687` n `230`; crypto_major avg `5.0448` n `8`; equity avg `-0.1314` n `120`; fx avg `-0.1948` n `6`; index avg `0.0234` n `25`; metal avg `0.8086` n `20`; unknown avg `0.5247` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
