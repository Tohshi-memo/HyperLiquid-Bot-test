# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T21:22:49.561956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.3074` n `228`; crypto_major avg `0.2721` n `8`; equity avg `0.0355` n `77`; fx avg `0.0044` n `6`; index avg `0.0485` n `23`; metal avg `-0.0045` n `18`; unknown avg `57.946` n `687`
- 1h: commodity avg `-0.2345` n `12`; crypto_alt avg `-0.0722` n `228`; crypto_major avg `-0.1399` n `8`; equity avg `-0.0621` n `77`; fx avg `0.022` n `6`; index avg `0.0184` n `23`; metal avg `-0.0766` n `18`; unknown avg `0.0927` n `679`
- 4h: commodity avg `0.3226` n `12`; crypto_alt avg `-0.8049` n `228`; crypto_major avg `-0.5358` n `8`; equity avg `-0.0898` n `77`; fx avg `-0.0152` n `6`; index avg `-0.0801` n `23`; metal avg `-0.2462` n `18`; unknown avg `-0.0053` n `679`
- 24h: commodity avg `0.3831` n `12`; crypto_alt avg `3.3086` n `228`; crypto_major avg `5.0922` n `8`; equity avg `2.593` n `76`; fx avg `0.0566` n `6`; index avg `1.2153` n `23`; metal avg `1.6799` n `18`; unknown avg `1.7273` n `519`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
