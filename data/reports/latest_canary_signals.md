# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T18:52:27.750804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0428` n `12`; crypto_alt avg `0.257` n `230`; crypto_major avg `0.3729` n `8`; equity avg `0.0082` n `96`; fx avg `-0.0067` n `6`; index avg `0.0015` n `25`; metal avg `-0.0323` n `20`; unknown avg `-0.0839` n `769`
- 1h: commodity avg `-0.0632` n `12`; crypto_alt avg `0.1139` n `230`; crypto_major avg `0.1592` n `8`; equity avg `-0.5718` n `96`; fx avg `0.0019` n `6`; index avg `-0.0369` n `25`; metal avg `-0.0155` n `20`; unknown avg `-0.1957` n `769`
- 4h: commodity avg `0.2496` n `12`; crypto_alt avg `0.8051` n `230`; crypto_major avg `0.9786` n `8`; equity avg `0.718` n `96`; fx avg `0.0721` n `6`; index avg `0.1166` n `25`; metal avg `0.127` n `20`; unknown avg `0.5368` n `769`
- 24h: commodity avg `0.7131` n `12`; crypto_alt avg `-0.8343` n `230`; crypto_major avg `-0.9927` n `8`; equity avg `-1.0634` n `94`; fx avg `0.086` n `6`; index avg `-0.1963` n `25`; metal avg `-0.0565` n `20`; unknown avg `0.0032` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
