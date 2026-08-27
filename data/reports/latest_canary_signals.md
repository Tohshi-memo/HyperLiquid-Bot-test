# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T16:22:41.419084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.1774` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5017` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.5393` n `231`; crypto_major avg `0.5536` n `8`; equity avg `-0.0936` n `127`; fx avg `-0.0014` n `6`; index avg `-0.0261` n `26`; metal avg `-0.0205` n `20`; unknown avg `-0.1208` n `792`
- 1h: commodity avg `0.0294` n `12`; crypto_alt avg `0.4528` n `231`; crypto_major avg `0.3755` n `8`; equity avg `0.0131` n `127`; fx avg `0.0018` n `6`; index avg `0.0004` n `26`; metal avg `0.1467` n `20`; unknown avg `-0.0757` n `792`
- 4h: commodity avg `0.0487` n `12`; crypto_alt avg `1.3759` n `231`; crypto_major avg `1.6892` n `8`; equity avg `-0.4882` n `127`; fx avg `0.0285` n `6`; index avg `-0.0581` n `26`; metal avg `0.1875` n `20`; unknown avg `-0.0865` n `792`
- 24h: commodity avg `-0.0896` n `12`; crypto_alt avg `4.3568` n `231`; crypto_major avg `4.9905` n `8`; equity avg `1.6774` n `127`; fx avg `-0.0667` n `6`; index avg `0.1903` n `26`; metal avg `0.1183` n `20`; unknown avg `0.8216` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
