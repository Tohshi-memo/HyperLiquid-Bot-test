# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T17:22:38.225529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.4681` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.3497` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5483` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0222` n `13`; crypto_alt avg `-0.0601` n `239`; crypto_major avg `0.0311` n `8`; equity avg `-0.1525` n `166`; fx avg `0.0119` n `6`; index avg `-0.009` n `27`; metal avg `-0.0146` n `20`; unknown avg `0.0909` n `1264`
- 1h: commodity avg `0.2692` n `13`; crypto_alt avg `-0.8661` n `239`; crypto_major avg `-0.9963` n `8`; equity avg `-0.5489` n `166`; fx avg `0.0016` n `6`; index avg `-0.059` n `27`; metal avg `-0.0915` n `20`; unknown avg `158.1547` n `1264`
- 4h: commodity avg `-0.3841` n `13`; crypto_alt avg `2.0256` n `239`; crypto_major avg `1.9656` n `8`; equity avg `4.4337` n `166`; fx avg `-0.1863` n `6`; index avg `0.5137` n `27`; metal avg `0.4173` n `20`; unknown avg `167.6724` n `1254`
- 24h: commodity avg `-1.3568` n `13`; crypto_alt avg `2.5668` n `239`; crypto_major avg `3.062` n `8`; equity avg `6.2441` n `166`; fx avg `-0.0643` n `6`; index avg `0.5724` n `27`; metal avg `0.7228` n `20`; unknown avg `188.5217` n `1059`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
