# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T22:37:26.848789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.9878` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5896` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1687` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0512` n `12`; crypto_alt avg `-0.0435` n `228`; crypto_major avg `-0.2355` n `8`; equity avg `0.0435` n `69`; fx avg `-0.0071` n `6`; index avg `0.0315` n `23`; metal avg `-0.0749` n `18`; unknown avg `-0.1864` n `422`
- 1h: commodity avg `-0.3945` n `12`; crypto_alt avg `-1.2154` n `228`; crypto_major avg `-1.1473` n `8`; equity avg `0.1481` n `69`; fx avg `-0.0032` n `6`; index avg `0.0214` n `23`; metal avg `-0.0473` n `18`; unknown avg `-0.7248` n `422`
- 4h: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.6066` n `228`; crypto_major avg `-1.3035` n `8`; equity avg `0.6843` n `69`; fx avg `-0.0067` n `6`; index avg `0.2861` n `23`; metal avg `0.0133` n `18`; unknown avg `-0.6566` n `422`
- 24h: commodity avg `-0.1189` n `12`; crypto_alt avg `-3.4004` n `228`; crypto_major avg `-5.1597` n `8`; equity avg `1.4214` n `69`; fx avg `0.0703` n `6`; index avg `0.8104` n `23`; metal avg `0.4063` n `18`; unknown avg `-0.2831` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
