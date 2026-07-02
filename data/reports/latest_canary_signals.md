# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T06:22:31.808051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6007` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0394` n `12`; crypto_alt avg `0.1745` n `228`; crypto_major avg `0.2538` n `8`; equity avg `-0.0777` n `88`; fx avg `0.0278` n `6`; index avg `0.0175` n `25`; metal avg `0.0745` n `20`; unknown avg `0.548` n `763`
- 1h: commodity avg `0.0047` n `12`; crypto_alt avg `-0.3338` n `228`; crypto_major avg `-0.2709` n `8`; equity avg `-0.8086` n `88`; fx avg `0.0047` n `6`; index avg `-0.195` n `25`; metal avg `0.1845` n `20`; unknown avg `0.0408` n `741`
- 4h: commodity avg `0.0168` n `12`; crypto_alt avg `0.2441` n `228`; crypto_major avg `0.4361` n `8`; equity avg `-1.1646` n `88`; fx avg `0.0063` n `6`; index avg `-0.2954` n `25`; metal avg `0.2344` n `20`; unknown avg `-0.4008` n `739`
- 24h: commodity avg `-0.4882` n `12`; crypto_alt avg `1.8263` n `228`; crypto_major avg `1.5424` n `8`; equity avg `-2.0306` n `88`; fx avg `-0.007` n `6`; index avg `-0.5298` n `25`; metal avg `1.3305` n `20`; unknown avg `24.9675` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
