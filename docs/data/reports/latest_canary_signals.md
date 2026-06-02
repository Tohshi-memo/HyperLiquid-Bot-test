# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T15:07:28.005146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.37` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `2.3403` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0434` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.6182` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.613` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-1.6106` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.5483` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1069` n `12`; crypto_alt avg `-0.4309` n `228`; crypto_major avg `-0.5513` n `8`; equity avg `-0.2464` n `69`; fx avg `-0.0146` n `6`; index avg `0.0503` n `23`; metal avg `0.0709` n `18`; unknown avg `0.6477` n `422`
- 1h: commodity avg `-0.2222` n `12`; crypto_alt avg `-1.9621` n `228`; crypto_major avg `-1.4969` n `8`; equity avg `0.0514` n `69`; fx avg `0.0166` n `6`; index avg `0.1213` n `23`; metal avg `0.1137` n `18`; unknown avg `0.0556` n `422`
- 4h: commodity avg `-0.017` n `12`; crypto_alt avg `-1.9875` n `228`; crypto_major avg `-1.9041` n `8`; equity avg `0.1393` n `69`; fx avg `-0.0114` n `6`; index avg `0.4362` n `23`; metal avg `-0.2911` n `18`; unknown avg `0.425` n `422`
- 24h: commodity avg `-1.2721` n `12`; crypto_alt avg `-1.3167` n `228`; crypto_major avg `-2.376` n `8`; equity avg `0.6048` n `69`; fx avg `0.1778` n `6`; index avg `0.6831` n `23`; metal avg `1.1135` n `18`; unknown avg `0.636` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
