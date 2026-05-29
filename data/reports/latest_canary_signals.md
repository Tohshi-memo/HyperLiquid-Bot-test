# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T16:37:26.685963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9154` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.664` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.2975` n `12`; crypto_alt avg `0.3831` n `228`; crypto_major avg `0.4592` n `8`; equity avg `0.0204` n `69`; fx avg `0.002` n `6`; index avg `-0.0097` n `23`; metal avg `0.1104` n `18`; unknown avg `0.177` n `419`
- 1h: commodity avg `-0.29` n `12`; crypto_alt avg `-0.1445` n `228`; crypto_major avg `0.0333` n `8`; equity avg `0.2497` n `69`; fx avg `-0.0218` n `6`; index avg `0.0914` n `23`; metal avg `-0.0286` n `18`; unknown avg `-0.203` n `418`
- 4h: commodity avg `-0.7879` n `12`; crypto_alt avg `2.2207` n `228`; crypto_major avg `2.1275` n `8`; equity avg `0.8621` n `69`; fx avg `0.0921` n `6`; index avg `-0.0939` n `23`; metal avg `0.4635` n `18`; unknown avg `0.7242` n `417`
- 24h: commodity avg `-0.7839` n `12`; crypto_alt avg `2.4044` n `228`; crypto_major avg `2.5333` n `8`; equity avg `2.1156` n `69`; fx avg `0.1936` n `6`; index avg `-0.0635` n `23`; metal avg `0.3993` n `18`; unknown avg `1.379` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1945`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
