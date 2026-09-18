# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T14:52:27.933105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.8551` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.6201` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1418` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0837` n `12`; crypto_alt avg `0.3084` n `234`; crypto_major avg `0.6024` n `8`; equity avg `0.1873` n `140`; fx avg `-0.0744` n `6`; index avg `0.0131` n `26`; metal avg `0.0708` n `20`; unknown avg `0.0086` n `928`
- 1h: commodity avg `-0.1214` n `12`; crypto_alt avg `0.2547` n `234`; crypto_major avg `0.747` n `8`; equity avg `-0.0622` n `140`; fx avg `-0.049` n `6`; index avg `-0.0505` n `26`; metal avg `0.0197` n `20`; unknown avg `0.8374` n `902`
- 4h: commodity avg `0.2985` n `12`; crypto_alt avg `0.8684` n `234`; crypto_major avg `2.4403` n `8`; equity avg `-0.4148` n `140`; fx avg `-0.0618` n `6`; index avg `-0.1448` n `26`; metal avg `-0.1798` n `20`; unknown avg `1.5553` n `893`
- 24h: commodity avg `0.1279` n `12`; crypto_alt avg `6.4039` n `234`; crypto_major avg `6.5368` n `8`; equity avg `0.6785` n `140`; fx avg `0.2028` n `6`; index avg `-0.0637` n `26`; metal avg `0.1239` n `20`; unknown avg `4.0881` n `729`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
