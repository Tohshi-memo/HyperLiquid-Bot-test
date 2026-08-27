# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T15:37:39.143566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.303` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6926` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0201` n `12`; crypto_alt avg `0.1267` n `231`; crypto_major avg `0.2344` n `8`; equity avg `-0.0606` n `127`; fx avg `-0.0046` n `6`; index avg `-0.0125` n `26`; metal avg `0.0616` n `20`; unknown avg `-0.0837` n `792`
- 1h: commodity avg `-0.1143` n `12`; crypto_alt avg `0.1524` n `231`; crypto_major avg `0.4035` n `8`; equity avg `-0.4141` n `127`; fx avg `-0.0142` n `6`; index avg `-0.0231` n `26`; metal avg `0.0733` n `20`; unknown avg `-0.1261` n `792`
- 4h: commodity avg `0.0547` n `12`; crypto_alt avg `1.2475` n `231`; crypto_major avg `1.7687` n `8`; equity avg `-0.5343` n `127`; fx avg `0.0296` n `6`; index avg `-0.054` n `26`; metal avg `0.0761` n `20`; unknown avg `-0.0637` n `792`
- 24h: commodity avg `0.1899` n `12`; crypto_alt avg `3.7172` n `231`; crypto_major avg `4.7039` n `8`; equity avg `1.4799` n `127`; fx avg `-0.0586` n `6`; index avg `0.1453` n `26`; metal avg `-0.0748` n `20`; unknown avg `0.7599` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
