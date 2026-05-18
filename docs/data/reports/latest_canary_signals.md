# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T01:52:13.173192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2959` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.0736` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9101` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8353` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.216` n `12`; crypto_alt avg `0.1372` n `228`; crypto_major avg `0.0984` n `8`; equity avg `0.4912` n `66`; fx avg `0.0085` n `5`; index avg `0.1239` n `23`; metal avg `0.6497` n `18`; unknown avg `1.0068` n `383`
- 1h: commodity avg `0.189` n `12`; crypto_alt avg `-0.0266` n `228`; crypto_major avg `-0.2368` n `8`; equity avg `0.6243` n `66`; fx avg `0.0419` n `5`; index avg `0.124` n `23`; metal avg `0.6455` n `18`; unknown avg `0.5669` n `383`
- 4h: commodity avg `0.9781` n `12`; crypto_alt avg `-2.6573` n `228`; crypto_major avg `-2.3178` n `8`; equity avg `-0.4077` n `66`; fx avg `0.099` n `5`; index avg `-0.4825` n `23`; metal avg `-0.2442` n `18`; unknown avg `2.7579` n `383`
- 24h: commodity avg `2.6769` n `12`; crypto_alt avg `-11.2429` n `228`; crypto_major avg `-3.3708` n `8`; equity avg `-3.2298` n `65`; fx avg `-0.084` n `5`; index avg `-1.8907` n `23`; metal avg `-6.16` n `18`; unknown avg `550.953` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
