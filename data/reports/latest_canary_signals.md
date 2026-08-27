# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T03:07:25.048926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0369` n `12`; crypto_alt avg `0.0689` n `231`; crypto_major avg `0.0518` n `8`; equity avg `-0.0209` n `126`; fx avg `0.0121` n `6`; index avg `-0.017` n `25`; metal avg `0.0163` n `20`; unknown avg `0.4459` n `793`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `-0.4804` n `231`; crypto_major avg `-0.4528` n `8`; equity avg `0.1892` n `126`; fx avg `0.0303` n `6`; index avg `0.0068` n `25`; metal avg `-0.0411` n `20`; unknown avg `0.0007` n `793`
- 4h: commodity avg `0.0198` n `12`; crypto_alt avg `-0.1252` n `231`; crypto_major avg `0.2483` n `8`; equity avg `-0.1228` n `126`; fx avg `-0.0289` n `6`; index avg `-0.0905` n `25`; metal avg `0.136` n `20`; unknown avg `0.2467` n `793`
- 24h: commodity avg `0.4491` n `12`; crypto_alt avg `0.0053` n `231`; crypto_major avg `0.382` n `8`; equity avg `1.3384` n `126`; fx avg `-0.1156` n `6`; index avg `0.1899` n `25`; metal avg `-0.2174` n `20`; unknown avg `0.4262` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
