# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T08:52:19.856502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1051` n `12`; crypto_alt avg `0.1206` n `228`; crypto_major avg `-0.0741` n `8`; equity avg `0.0102` n `67`; fx avg `0.0021` n `6`; index avg `0.0214` n `23`; metal avg `-0.0225` n `18`; unknown avg `0.9222` n `397`
- 1h: commodity avg `0.0592` n `12`; crypto_alt avg `0.2513` n `228`; crypto_major avg `0.1347` n `8`; equity avg `0.0254` n `67`; fx avg `0.0145` n `6`; index avg `0.0135` n `23`; metal avg `-0.0673` n `18`; unknown avg `0.94` n `397`
- 4h: commodity avg `0.4033` n `12`; crypto_alt avg `0.5347` n `228`; crypto_major avg `0.2646` n `8`; equity avg `0.0294` n `67`; fx avg `0.0759` n `6`; index avg `0.0679` n `23`; metal avg `-0.1034` n `18`; unknown avg `1.2297` n `387`
- 24h: commodity avg `0.1522` n `12`; crypto_alt avg `0.2934` n `228`; crypto_major avg `0.1196` n `8`; equity avg `0.468` n `67`; fx avg `0.0007` n `6`; index avg `-0.0693` n `23`; metal avg `0.4308` n `18`; unknown avg `-0.0489` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
