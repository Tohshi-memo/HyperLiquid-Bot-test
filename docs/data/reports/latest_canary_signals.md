# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T01:52:30.804834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_crypto_metal_divergence: score `1.6466` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.1051` n `230`; crypto_major avg `0.1065` n `8`; equity avg `0.0332` n `121`; fx avg `-0.0014` n `6`; index avg `0.0081` n `25`; metal avg `0.0036` n `20`; unknown avg `3.5437` n `794`
- 1h: commodity avg `-0.0201` n `12`; crypto_alt avg `-0.7548` n `230`; crypto_major avg `-0.3601` n `8`; equity avg `0.0246` n `121`; fx avg `-0.0101` n `6`; index avg `0.0115` n `25`; metal avg `0.0152` n `20`; unknown avg `3.9263` n `794`
- 4h: commodity avg `-0.0301` n `12`; crypto_alt avg `1.036` n `230`; crypto_major avg `1.6606` n `8`; equity avg `0.225` n `121`; fx avg `0.0323` n `6`; index avg `0.0313` n `25`; metal avg `0.014` n `20`; unknown avg `3.4728` n `794`
- 24h: commodity avg `0.0651` n `12`; crypto_alt avg `-2.7066` n `230`; crypto_major avg `1.1284` n `8`; equity avg `-0.18` n `121`; fx avg `0.0931` n `6`; index avg `-0.0387` n `25`; metal avg `-0.0259` n `20`; unknown avg `3.0304` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
