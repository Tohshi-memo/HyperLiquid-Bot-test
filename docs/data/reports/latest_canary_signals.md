# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T08:07:26.442551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.66` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.5935` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0414` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0148` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.1309` n `228`; crypto_major avg `-0.1619` n `8`; equity avg `0.1132` n `69`; fx avg `0.0064` n `6`; index avg `0.0338` n `23`; metal avg `0.1` n `18`; unknown avg `-0.0347` n `422`
- 1h: commodity avg `-0.0941` n `12`; crypto_alt avg `0.4461` n `228`; crypto_major avg `0.2753` n `8`; equity avg `0.2215` n `69`; fx avg `0.01` n `6`; index avg `0.1052` n `23`; metal avg `0.1066` n `18`; unknown avg `-0.1014` n `422`
- 4h: commodity avg `-0.1421` n `12`; crypto_alt avg `-1.1852` n `228`; crypto_major avg `-1.4739` n `8`; equity avg `0.5409` n `69`; fx avg `0.0707` n `6`; index avg `0.5675` n `23`; metal avg `1.1196` n `18`; unknown avg `0.1296` n `412`
- 24h: commodity avg `-1.1013` n `12`; crypto_alt avg `0.1654` n `228`; crypto_major avg `-1.3108` n `8`; equity avg `0.5878` n `69`; fx avg `0.149` n `6`; index avg `-0.0657` n `23`; metal avg `1.3888` n `18`; unknown avg `1.4093` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1931`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
