# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T11:22:29.075227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4794` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2545` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5016` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0553` n `12`; crypto_alt avg `0.1583` n `229`; crypto_major avg `0.2603` n `8`; equity avg `0.0404` n `88`; fx avg `-0.0116` n `6`; index avg `0.0024` n `25`; metal avg `0.108` n `20`; unknown avg `-0.0853` n `763`
- 1h: commodity avg `-0.0983` n `12`; crypto_alt avg `0.2938` n `229`; crypto_major avg `0.7385` n `8`; equity avg `0.2444` n `88`; fx avg `0.0057` n `6`; index avg `0.0371` n `25`; metal avg `-0.0468` n `20`; unknown avg `-0.0216` n `763`
- 4h: commodity avg `-0.0768` n `12`; crypto_alt avg `1.5636` n `228`; crypto_major avg `2.4026` n `8`; equity avg `0.901` n `88`; fx avg `-0.042` n `6`; index avg `0.0873` n `25`; metal avg `0.1481` n `20`; unknown avg `0.8098` n `763`
- 24h: commodity avg `-0.572` n `12`; crypto_alt avg `3.0548` n `228`; crypto_major avg `4.1182` n `8`; equity avg `-1.9454` n `88`; fx avg `-0.123` n `6`; index avg `-0.584` n `25`; metal avg `0.6628` n `20`; unknown avg `2.7848` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
