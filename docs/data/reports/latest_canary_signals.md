# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T10:22:15.911682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.9205` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.7086` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `0.0105` n `228`; crypto_major avg `0.0996` n `8`; equity avg `0.0535` n `65`; fx avg `0.0068` n `5`; index avg `0.0449` n `23`; metal avg `0.0003` n `18`; unknown avg `0.0828` n `383`
- 1h: commodity avg `0.0146` n `12`; crypto_alt avg `0.3142` n `228`; crypto_major avg `0.4122` n `8`; equity avg `0.1543` n `65`; fx avg `0.002` n `5`; index avg `0.0672` n `23`; metal avg `-0.0107` n `18`; unknown avg `0.1685` n `383`
- 4h: commodity avg `1.7843` n `12`; crypto_alt avg `-8.6015` n `228`; crypto_major avg `-2.1362` n `8`; equity avg `-2.667` n `65`; fx avg `-0.1689` n `5`; index avg `-1.6912` n `23`; metal avg `-5.8448` n `18`; unknown avg `550.2282` n `367`
- 24h: commodity avg `1.7843` n `12`; crypto_alt avg `-8.6015` n `228`; crypto_major avg `-2.1362` n `8`; equity avg `-2.667` n `65`; fx avg `-0.1689` n `5`; index avg `-1.6912` n `23`; metal avg `-5.8448` n `18`; unknown avg `550.2282` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
