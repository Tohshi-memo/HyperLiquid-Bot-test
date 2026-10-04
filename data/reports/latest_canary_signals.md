# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T15:37:27.795982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `13`; crypto_alt avg `-0.1517` n `235`; crypto_major avg `-0.1242` n `8`; equity avg `-0.0118` n `144`; fx avg `0.0231` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0109` n `20`; unknown avg `0.5609` n `1078`
- 1h: commodity avg `-0.017` n `13`; crypto_alt avg `-0.1543` n `235`; crypto_major avg `0.1481` n `8`; equity avg `0.0182` n `144`; fx avg `0.0266` n `6`; index avg `-0.0134` n `26`; metal avg `-0.0049` n `20`; unknown avg `0.521` n `1076`
- 4h: commodity avg `-0.0415` n `13`; crypto_alt avg `0.1466` n `235`; crypto_major avg `0.024` n `8`; equity avg `0.0382` n `144`; fx avg `0.03` n `6`; index avg `-0.0204` n `26`; metal avg `-0.008` n `20`; unknown avg `0.1353` n `1070`
- 24h: commodity avg `-0.0414` n `13`; crypto_alt avg `1.1711` n `235`; crypto_major avg `0.9771` n `8`; equity avg `0.2666` n `144`; fx avg `0.037` n `6`; index avg `0.0035` n `26`; metal avg `0.0013` n `20`; unknown avg `0.0845` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2041`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
