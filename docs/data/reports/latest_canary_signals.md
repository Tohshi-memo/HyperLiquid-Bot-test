# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T09:07:35.159927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `-1.874` n `230`; crypto_major avg `-2.014` n `8`; equity avg `-0.203` n `121`; fx avg `-0.0022` n `6`; index avg `-0.0235` n `25`; metal avg `0.0331` n `20`; unknown avg `0.7967` n `793`
- 1h: commodity avg `-0.1439` n `12`; crypto_alt avg `-0.2977` n `230`; crypto_major avg `0.1833` n `8`; equity avg `0.0165` n `121`; fx avg `-0.0024` n `6`; index avg `-0.0261` n `25`; metal avg `0.1844` n `20`; unknown avg `0.9801` n `793`
- 4h: commodity avg `0.0655` n `12`; crypto_alt avg `1.9569` n `230`; crypto_major avg `1.6407` n `8`; equity avg `0.4237` n `121`; fx avg `-0.0046` n `6`; index avg `0.0209` n `25`; metal avg `0.3596` n `20`; unknown avg `0.9066` n `777`
- 24h: commodity avg `0.0208` n `12`; crypto_alt avg `5.7421` n `230`; crypto_major avg `5.721` n `8`; equity avg `0.3281` n `121`; fx avg `-0.103` n `6`; index avg `0.0226` n `25`; metal avg `0.9565` n `20`; unknown avg `3.3656` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1981`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
