# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T12:37:31.051484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6149` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `0.0808` n `8`; equity avg `0.312` n `102`; fx avg `0.0068` n `6`; index avg `0.0306` n `25`; metal avg `0.0157` n `20`; unknown avg `-0.0024` n `779`
- 1h: commodity avg `0.0242` n `12`; crypto_alt avg `0.1762` n `230`; crypto_major avg `0.2336` n `8`; equity avg `0.7732` n `102`; fx avg `0.0267` n `6`; index avg `0.0868` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.0518` n `779`
- 4h: commodity avg `-0.2056` n `12`; crypto_alt avg `0.1162` n `230`; crypto_major avg `0.4381` n `8`; equity avg `2.053` n `102`; fx avg `-0.0421` n `6`; index avg `0.2783` n `25`; metal avg `0.1368` n `20`; unknown avg `0.0515` n `771`
- 24h: commodity avg `0.0405` n `12`; crypto_alt avg `0.3302` n `230`; crypto_major avg `0.4598` n `8`; equity avg `-0.8189` n `102`; fx avg `-0.0415` n `6`; index avg `-0.0972` n `25`; metal avg `0.5939` n `20`; unknown avg `-0.1477` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
