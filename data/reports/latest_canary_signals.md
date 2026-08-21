# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T22:46:01.240930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.9696` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.9511` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.814` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.0424` n `230`; crypto_major avg `0.0371` n `8`; equity avg `-0.014` n `121`; fx avg `-0.0037` n `6`; index avg `0.0007` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0787` n `793`
- 1h: commodity avg `0.0357` n `12`; crypto_alt avg `0.461` n `230`; crypto_major avg `0.7072` n `8`; equity avg `-0.0001` n `121`; fx avg `-0.0104` n `6`; index avg `0.0111` n `25`; metal avg `-0.0168` n `20`; unknown avg `1.6399` n `793`
- 4h: commodity avg `-0.0426` n `12`; crypto_alt avg `2.6812` n `230`; crypto_major avg `3.9085` n `8`; equity avg `0.0945` n `121`; fx avg `-0.0078` n `6`; index avg `0.0067` n `25`; metal avg `-0.0611` n `20`; unknown avg `1.3389` n `793`
- 24h: commodity avg `0.1709` n `12`; crypto_alt avg `8.8244` n `230`; crypto_major avg `8.1617` n `8`; equity avg `0.9128` n `121`; fx avg `-0.0669` n `6`; index avg `0.098` n `25`; metal avg `0.455` n `20`; unknown avg `2.5392` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
