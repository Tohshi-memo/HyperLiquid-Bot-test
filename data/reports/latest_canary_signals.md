# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T01:52:20.143842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0771` n `12`; crypto_alt avg `0.0279` n `228`; crypto_major avg `0.0621` n `8`; equity avg `-0.2774` n `69`; fx avg `0.0198` n `6`; index avg `-0.2096` n `23`; metal avg `-0.6733` n `18`; unknown avg `0.5438` n `422`
- 1h: commodity avg `-0.1101` n `12`; crypto_alt avg `-0.6994` n `228`; crypto_major avg `-0.6821` n `8`; equity avg `-0.1789` n `69`; fx avg `0.0308` n `6`; index avg `-0.179` n `23`; metal avg `-0.3023` n `18`; unknown avg `0.3689` n `422`
- 4h: commodity avg `-0.4557` n `12`; crypto_alt avg `-0.6899` n `228`; crypto_major avg `-0.3665` n `8`; equity avg `-1.0393` n `69`; fx avg `0.058` n `6`; index avg `-0.5546` n `23`; metal avg `-0.3312` n `18`; unknown avg `0.5078` n `422`
- 24h: commodity avg `-0.4189` n `12`; crypto_alt avg `-0.9011` n `228`; crypto_major avg `-1.2217` n `8`; equity avg `-1.0905` n `69`; fx avg `0.0271` n `6`; index avg `-0.6352` n `23`; metal avg `-0.7446` n `18`; unknown avg `2.1267` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
