# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T22:10:51.172781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.49` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.4231` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.066` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8648` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1756` n `12`; crypto_alt avg `-0.6374` n `228`; crypto_major avg `-0.4359` n `8`; equity avg `0.1267` n `69`; fx avg `-0.0031` n `6`; index avg `-0.0437` n `23`; metal avg `0.0317` n `18`; unknown avg `-0.373` n `422`
- 1h: commodity avg `0.1622` n `12`; crypto_alt avg `-0.7276` n `228`; crypto_major avg `-0.6739` n `8`; equity avg `0.0855` n `69`; fx avg `-0.009` n `6`; index avg `-0.0124` n `23`; metal avg `0.0336` n `18`; unknown avg `0.5349` n `422`
- 4h: commodity avg `0.153` n `12`; crypto_alt avg `-1.6015` n `228`; crypto_major avg `-1.772` n `8`; equity avg `0.6511` n `69`; fx avg `-0.0167` n `6`; index avg `0.294` n `23`; metal avg `0.0928` n `18`; unknown avg `0.3659` n `422`
- 24h: commodity avg `0.0052` n `12`; crypto_alt avg `-3.4146` n `228`; crypto_major avg `-4.7303` n `8`; equity avg `1.3749` n `69`; fx avg `0.074` n `6`; index avg `0.795` n `23`; metal avg `0.5245` n `18`; unknown avg `0.5764` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
