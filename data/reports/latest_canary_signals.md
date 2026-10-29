# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T20:22:29.403222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.207` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9718` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7892` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0294` n `13`; crypto_alt avg `0.268` n `238`; crypto_major avg `0.2346` n `8`; equity avg `0.3841` n `156`; fx avg `0.0157` n `6`; index avg `0.0224` n `27`; metal avg `0.0006` n `20`; unknown avg `124.118` n `1210`
- 1h: commodity avg `0.0949` n `13`; crypto_alt avg `-0.9384` n `238`; crypto_major avg `-0.7235` n `8`; equity avg `-0.9912` n `156`; fx avg `0.0169` n `6`; index avg `-0.1125` n `27`; metal avg `0.07` n `20`; unknown avg `2.9496` n `1182`
- 4h: commodity avg `0.2443` n `13`; crypto_alt avg `-2.6703` n `238`; crypto_major avg `-1.9627` n `8`; equity avg `-1.9931` n `156`; fx avg `0.0074` n `6`; index avg `-0.1735` n `27`; metal avg `0.0091` n `20`; unknown avg `8.9479` n `1184`
- 24h: commodity avg `-0.1146` n `13`; crypto_alt avg `-2.413` n `238`; crypto_major avg `0.0864` n `8`; equity avg `-2.4732` n `155`; fx avg `0.0506` n `6`; index avg `-0.3043` n `27`; metal avg `-0.6042` n `20`; unknown avg `32.9222` n `964`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
