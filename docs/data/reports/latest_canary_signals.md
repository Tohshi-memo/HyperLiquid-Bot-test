# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T02:52:25.627990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `2.3602` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `2.3353` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `2.2665` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0034` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9852` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9033` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `0.4307` n `230`; crypto_major avg `0.7892` n `8`; equity avg `0.0536` n `121`; fx avg `0.0021` n `6`; index avg `0.0012` n `25`; metal avg `-0.0061` n `20`; unknown avg `2.0159` n `793`
- 1h: commodity avg `0.0138` n `12`; crypto_alt avg `1.9259` n `230`; crypto_major avg `2.3491` n `8`; equity avg `0.0826` n `121`; fx avg `0.0085` n `6`; index avg `0.0019` n `25`; metal avg `-0.0111` n `20`; unknown avg `0.0471` n `793`
- 4h: commodity avg `-0.0436` n `12`; crypto_alt avg `2.5041` n `230`; crypto_major avg `1.9598` n `8`; equity avg `0.0565` n `121`; fx avg `0.0239` n `6`; index avg `0.0039` n `25`; metal avg `-0.0254` n `20`; unknown avg `0.2363` n `793`
- 24h: commodity avg `0.0546` n `12`; crypto_alt avg `10.602` n `230`; crypto_major avg `8.6958` n `8`; equity avg `0.0605` n `121`; fx avg `0.0466` n `6`; index avg `-0.0258` n `25`; metal avg `0.1404` n `20`; unknown avg `1.3285` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
