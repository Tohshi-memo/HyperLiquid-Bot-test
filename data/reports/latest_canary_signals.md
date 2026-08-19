# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T17:22:28.579953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `4.746` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.2456` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.1401` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0419` n `12`; crypto_alt avg `-0.1753` n `230`; crypto_major avg `-0.287` n `8`; equity avg `-0.1732` n `121`; fx avg `-0.0036` n `6`; index avg `-0.0309` n `25`; metal avg `-0.0183` n `20`; unknown avg `0.16` n `792`
- 1h: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.2795` n `230`; crypto_major avg `-0.7266` n `8`; equity avg `-0.6139` n `121`; fx avg `-0.0219` n `6`; index avg `-0.0916` n `25`; metal avg `-0.0659` n `20`; unknown avg `-0.0445` n `792`
- 4h: commodity avg `0.1272` n `12`; crypto_alt avg `2.1249` n `230`; crypto_major avg `3.3728` n `8`; equity avg `-1.3732` n `121`; fx avg `0.0409` n `6`; index avg `-0.2231` n `25`; metal avg `0.2327` n `20`; unknown avg `0.5386` n `792`
- 24h: commodity avg `0.3918` n `12`; crypto_alt avg `2.4794` n `230`; crypto_major avg `4.3116` n `8`; equity avg `-0.6387` n `120`; fx avg `-0.1857` n `6`; index avg `-0.0415` n `25`; metal avg `0.7394` n `20`; unknown avg `0.476` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
