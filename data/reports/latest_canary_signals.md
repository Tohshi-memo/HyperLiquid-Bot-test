# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T16:22:26.047571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.29` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.4189` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2872` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.2335` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2008` n `12`; crypto_alt avg `0.7074` n `228`; crypto_major avg `0.2963` n `8`; equity avg `0.1499` n `69`; fx avg `-0.0117` n `6`; index avg `-0.0687` n `23`; metal avg `-0.1591` n `18`; unknown avg `1.4639` n `422`
- 1h: commodity avg `0.4958` n `12`; crypto_alt avg `0.4916` n `228`; crypto_major avg `0.1732` n `8`; equity avg `0.28` n `69`; fx avg `0.0067` n `6`; index avg `0.0479` n `23`; metal avg `-0.2219` n `18`; unknown avg `1.8162` n `422`
- 4h: commodity avg `0.5485` n `12`; crypto_alt avg `-1.8438` n `228`; crypto_major avg `-1.8704` n `8`; equity avg `0.3631` n `69`; fx avg `-0.0038` n `6`; index avg `0.4168` n `23`; metal avg `-0.5205` n `18`; unknown avg `1.1038` n `422`
- 24h: commodity avg `-0.9456` n `12`; crypto_alt avg `-1.6281` n `228`; crypto_major avg `-2.077` n `8`; equity avg `0.9143` n `69`; fx avg `0.1433` n `6`; index avg `0.673` n `23`; metal avg `0.9281` n `18`; unknown avg `0.1641` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
