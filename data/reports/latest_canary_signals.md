# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T09:22:25.905177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5983` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3557` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.23` n `12`; crypto_alt avg `0.5587` n `228`; crypto_major avg `0.4117` n `8`; equity avg `0.1424` n `74`; fx avg `0.0161` n `6`; index avg `0.1173` n `23`; metal avg `0.1903` n `18`; unknown avg `1.1244` n `424`
- 1h: commodity avg `-0.0155` n `12`; crypto_alt avg `0.3595` n `228`; crypto_major avg `0.4218` n `8`; equity avg `0.173` n `74`; fx avg `0.0157` n `6`; index avg `0.0908` n `23`; metal avg `0.149` n `18`; unknown avg `0.0418` n `424`
- 4h: commodity avg `-0.4589` n `12`; crypto_alt avg `-2.5938` n `228`; crypto_major avg `-1.309` n `8`; equity avg `-0.0883` n `74`; fx avg `0.0672` n `6`; index avg `0.0467` n `23`; metal avg `0.2893` n `18`; unknown avg `-0.0286` n `404`
- 24h: commodity avg `-0.5512` n `12`; crypto_alt avg `-4.1036` n `228`; crypto_major avg `-2.5739` n `8`; equity avg `0.0331` n `73`; fx avg `0.1182` n `6`; index avg `0.0813` n `23`; metal avg `-0.2661` n `18`; unknown avg `-0.1625` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
